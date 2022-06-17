# -*- coding: utf-8 -*-

__doc__ = 'Implementation of image based mesh generation.'

from math import sqrt
import sys
import warnings

import numpy as np

from ..basis import BSplineBasis
from .. import curve_factory, surface_factory


def get_corners(X, L=50, R=30, D=15):
    """Detects corners of traced outlines using the SAM04 algorithm.

    The outline is assumed to constitute a discrete closed curve where each
    point is included just once. Increasing `D` and `R` will give the same
    number of corners or fewer corners.

    :param numpy.array X: A traced outline forming a discrete closed curve
        (size *n* × 2)
    :param float L: Controls the scale at which corners are measured.
    :param float R: Controls how close corners can appear.
    :param float D: The lower bound for the corner metric. Corner candidates
        with lower metric than this are rejected.
    :return: The indices of X that consitute corner points
    :rtype: numpy.array
    """
    n = len(X)

    # Finds corner candidates
    d = np.zeros(n)
    for i in range(1,n+1):
        if i+L <= n:
            k = i+L
            index = np.array(range(i+1,k))
        else:
            k = i+L-n
            index = np.array(list(range(i+1,n+1)) + list(range(1,k)))

        M = X[k-1,:]-X[i-1,:]

        if M[0] == 0:
            dCand = abs(X[index-1,0]-X[i-1,0])
        else:
            m = float(M[1])/M[0]
            dCand = abs(X[index-1,1]-m*X[index-1,0]+m*X[i-1,0]-X[i-1,1])/sqrt(m**2+1)

        Y = max(dCand)
        I = np.argmax(dCand)
        if Y > d[index[I]-1]:
            d[index[I]-1] = Y

    I = np.where(d > 0)[0]
    # Rejects candidates which do not meet the lower metric bound D.
    index  = d <  D
    index2 = d >= D
    d[index] = 0
    C = np.array(range(n))
    C = C[index2]


    # Rejects corners that are too close to a corner with larger metric.
    l = len(C)
    j = 0
    while j+1 < l:
        if abs(C[j]-C[j+1]) <= R:
            if d[C[j]] > d[C[j+1]]:
                C = np.delete(C, j+1)
            else:
                C = np.delete(C, j)
            l = l-1
        else:
            j = j+1

    if l > 0 and abs(C[0]+n-C[-1]) <=R:
        if d[C[-1]] > d[C[0]]:
            C = C[1:-1]
        else:
            C = C[0:-2]

    # always include end-points in corner list, and never closer than 4 indices
    if 0 not in C:
        C = np.insert(C,0,0)
    if (n-1) not in C:
        C = np.append(C,n-1)
    remove = []
    for i in range(1,len(C)-1):
        if C[i]-C[i-1] < 5:
            remove.append(i)
    if C[-1]-C[-2] < 5 and len(C)-2 not in remove:
        remove.append(len(C)-2)

    remove.reverse()
    for j in remove:
        C = np.delete(C,j)

    return C


def image_curves(filename):
    """Generate B-spline curves corresponding to the edges in a black/white
    mask image.

    :param str filename: Name of image file to read
    :return: All curves generated by tracing the black/white edges
    :rtype: [:class:`splipy.Curve`]
    """
    import cv2

    im = cv2.imread(filename)

    # initialize image holders
    imGrey   = np.zeros((len(im),   len(im[0])),   np.uint8)
    imBlack  = np.zeros((len(im),   len(im[0])),   np.uint8)

    # convert to greyscale image
    cv2.cvtColor(im, cv2.COLOR_RGB2GRAY, imGrey)

    # convert to binary black/white
    cv2.threshold(imGrey, 128, 255, cv2.THRESH_BINARY, imBlack)

    # find contour curves in image
    if cv2.__version__[0] == '3':
        warnings.warn(FutureWarning('openCV v.3 will eventually be discontinued. Please update your version: \"pip install opencv-python --upgrade\"'))
        [_, contours, _] = cv2.findContours(imBlack, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    else:
        [contours, _]    = cv2.findContours(imBlack, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    result = []
    for i in range(len(contours)-1):   # for all contours (except the last one which is the edge)
        pts = contours[i][:,0,:]       # I have no idea why there needs to be a 0 here
        for j in range(len(pts)):      # invert y-axis since images are stored the other way around
            pts[j][1] = len(im[0])-pts[j][1]

        corners = get_corners(pts)
        if len(corners)>2:                        # start/stop tagged as corners. If any inner corners, then
            pts     = np.roll(pts, -corners[1],0) # rearrange points so start/stop falls at a natural corner.
            corners = get_corners(pts)            # recompute corners, since previous sem might be smooth

        n = len(pts)
        parpt = list(range(n))
        for i in range(n):
            parpt[i] = float(parpt[i]) / (n-1)

        # the choice of knot vector is a tricky one. We'll go with the following strategy:
        # - cubic, p=3 curve
        # - C^0 at corner points (computed above)
        # - at least one C^2 knot between corner knots
        # - otherwise as uniform as possible
        # - starts at 0, ends at 1
        # - around 1/10 the number of control points wrt points
        # - up to a max of 100(ish) control points for large models

        # start off with a uniform(ish) knot vector
        knot = []
        nStart = min(n//10, 90)
        for i in range(nStart+1):
            knot.append(int(1.0*i*(n-1)/nStart))
        c = corners.tolist()
        knot = sorted(list(set(knot+c))) # unique sorted list

        # make sure there is at least one knot between corners
        newKnot = []
        for i in range(len(c)-1):
            if knot.index(c[i+1])-knot.index(c[i]) == 1:
                newKnot.append((c[i+1]+c[i])/2)
        knot = sorted(knot + newKnot)

        # make sure no two knots are too close (typical corners which do this)
        for i in range(1,len(knot)-1):
            if knot[i] not in c:
                knot[i] = (knot[i-1]+knot[i+1])/2.0

        # make C^0 at corners and C^-1 at endpoints by duplicating knots
        knot = sorted(knot + c + c + [0,n-1]) # both c and knot contains a copy of the endpoints

        # make it span [0,1] instead of [0,n-1]
        for i in range(len(knot)):
            knot[i] /= float(n-1)

        # make it periodic since these are all closed curves
        knot[0]  -= knot[-1] - knot[-5]
        knot[-1] += knot[4]  - knot[1]

        basis = BSplineBasis(4, knot, 0)

        c = curve_factory.least_square_fit(np.array(pts), basis, parpt)
        result.append(c)

    return result

def image_height(filename, N=[30,30], p=[4,4]):
    """Generate a B-spline surface approximation given by the heightmap in a
    grayscale image.

    :param str filename: Name of image file to read
    :param (int,int) N: Number of controlpoints in u-direction
    :param (int,int) p: Polynomial order (degree+1)
    :return: Normalized (all values between 0 and 1) heightmap approximation
    :rtype: :class:`splipy.Surface`
    """

    import cv2

    im = cv2.imread(filename)

    width  = len(im[0])
    height = len(im)

    # initialize image holder
    imGrey = np.zeros((height, width), np.uint8)

    # convert to greyscale image
    cv2.cvtColor(im, cv2.COLOR_RGB2GRAY, imGrey)

    # guess uniform evaluation points and knot vectors
    u = list(range(width))
    v = list(range(height))
    knot1 = [0]*(p[0]-1) + list(range(N[0]-p[0]+2)) + [N[0]-p[0]+1]*(p[0]-1)
    knot2 = [0]*(p[1]-1) + list(range(N[1]-p[1]+2)) + [N[1]-p[1]+1]*(p[1]-1)

    # normalize all values to be in range [0, 1]
    u     = [float(i)/u[-1]     for i in u]
    v     = [float(i)/v[-1]     for i in v]
    knot1 = [float(i)/knot1[-1] for i in knot1]
    knot2 = [float(i)/knot2[-1] for i in knot2]

    # flip and reverse image so coordinate (0,0) is at lower-left corner
    imGrey = imGrey.T  / 255.0
    imGrey = np.flip(imGrey, axis=1)
    x,y    = np.meshgrid(u,v, indexing='ij')
    pts   = np.stack([x,y,imGrey], axis=2)

    basis1 = BSplineBasis(p[0], knot1)
    basis2 = BSplineBasis(p[1], knot2)

    return surface_factory.least_square_fit(pts,[basis1, basis2], [u,v])

def image_convex_surface(filename):
    """Generate a single B-spline surface corresponding to convex black domain
    of a black/white mask image. The algorithm traces the boundary and searches
    for 4 natural corner points. It will then generate 4 boundary curves which
    will be used to create the surface by Coons Patch.

    :param str filename: Name of image file to read
    :return: B-spline surface
    :rtype: :class:`splipy.Surface`
    """
    # generate boundary curve
    crv = image_curves(filename)

    # error test input
    if len(crv) != 1:
        raise RuntimeError('Error: image_convex_surface expects a single closed curve. Multiple curves detected')

    crv = crv[0]

    # parametric value of corner candidates. These are all in the range [0,1] and both 0 and 1 is present
    kinks = crv.get_kinks()

    # generate 4 corners
    if len(kinks) == 2:
        corners = [0, .25, .5, .75]

    elif len(kinks) == 3:
        corners = [0, (0+kinks[1])/2, kinks[1], (1+kinks[1])/2]

    elif len(kinks) == 4:
        if kinks[1]-kinks[0] > kinks[2]-kinks[1] and kinks[1]-kinks[0] > kinks[3]-kinks[2]:
            corners = [0, (kinks[0]+kinks[1])/2] + kinks[1:3]
        elif kinks[2]-kinks[1] > kinks[3]-kinks[2]:
            corners = [0, kinks[1], (kinks[1]+kinks[2])/2], kinks[2]
        else:
            corners = [0] + kinks[1:3] + [(kinks[2]+kinks[3])/2]

    else:
        while len(kinks) > 5:
            max_span   = 0
            max_span_i = 0
            for i in range(1,len(kinks)-1):
                max_span   = max(max_span, kinks[i+1]-kinks[i-1])
                max_span_i = i
            del kinks[max_span_i]
        corners = kinks[0:4]

    return surface_factory.edge_curves(crv.split(corners))
