import json

nodes = { 0: "A0", 1: "B0", 2: "C0", 3: "D0", 4: "A1", 5: "B1", 6: "C1", 7: "D1", 8: "A2", 9: "B2", 10: "C2", 11: "D2", 12: "A3", 13: "B3", 14: "C3",
15: "D3", 16: "A4", 17: "B4", 18: "C4", 19: "D4", 20: "A5", 21: "B5", 22: "C5", 23: "D5", 24: "A6", 25: "B6", 26: "C6", 27: "D6", 28: "A7", 29: "B7",
30: "C7", 31: "D7", 32: "F0", 33: "F1", 34: "F2", 35: "F3", 36: "F4", 37: "F5", 38: "F6", 39: "F7", 40: "Q0", 41: "Q1", 42: "Q2", 43: "Q3", 44: "Q4",
45: "Q5", 46: "Q6", 47: "Q7", 48: "OF0", 49: "OF1", 50: "OF2", 51: "OF3", 52: "OF4", 53: "OF5", 54: "OF6", 55: "OF7", 56: "X01", 57: "X02", 58: "X03",
59: "X04", 60: "X05", 61: "X06", 62: "X07", 63: "X08", 64: "N100", 65: "SN10", 66: "SN20", 67: "N130", 68: "S100", 69: "S130", 70: "E100", 71: "EW10",
72: "EW20", 73: "E130", 74: "W100", 75: "W130", 76: "N200", 77: "N210", 78: "N220", 79: "N230", 80: "N240", 81: "N250", 82: "N260", 83: "N270", 84: "S200",
85: "S210", 86: "S220", 87: "S230", 88: "S240", 89: "S250", 90: "S260", 91: "S270", 92: "E200", 93: "E210", 94: "E220", 95: "E230", 96: "E240", 97: "E250",
98: "E260", 99: "E270", 100: "W200", 101: "W210", 102: "W220", 103: "W230", 104: "W240", 105: "W250", 106: "W260", 107: "W270", 108: "N800", 109: "N810",
110: "N820", 111: "N830", 112: "S800", 113: "S810", 114: "S820", 115: "S830", 116: "E800", 117: "E810", 118: "E820", 119: "E830", 120: "W800", 121: "W810",
122: "W820", 123: "W830", 124: "CLK0", 125: "CLK1", 126: "CLK2", 127: "LSR0", 128: "LSR1", 129: "LSR2", 130: "CE0", 131: "CE1", 132: "CE2", 133: "SEL0",
134: "SEL1", 135: "SEL2", 136: "SEL3", 137: "SEL4", 138: "SEL5", 139: "SEL6", 140: "SEL7", 141: "N101", 142: "N131", 143: "S101", 144: "S131", 145: "E101", 146: "E131",
147: "W101", 148: "W131", 149: "N201", 150: "N211", 151: "N221", 152: "N231", 153: "N241", 154: "N251", 155: "N261", 156: "N271", 157: "S201", 158: "S211",
159: "S221", 160: "S231", 161: "S241", 162: "S251", 163: "S261", 164: "S271", 165: "E201", 166: "E211", 167: "E221", 168: "E231", 169: "E241", 170: "E251",
171: "E261", 172: "E271", 173: "W201", 174: "W211", 175: "W221", 176: "W231", 177: "W241", 178: "W251", 179: "W261", 180: "W271", 181: "N202", 182: "N212",
183: "N222", 184: "N232", 185: "N242", 186: "N252", 187: "N262", 188: "N272", 189: "S202", 190: "S212", 191: "S222", 192: "S232", 193: "S242", 194: "S252",
195: "S262", 196: "S272", 197: "E202", 198: "E212", 199: "E222", 200: "E232", 201: "E242", 202: "E252", 203: "E262", 204: "E272", 205: "W202", 206: "W212",
207: "W222", 208: "W232", 209: "W242", 210: "W252", 211: "W262", 212: "W272", 213: "N804", 214: "N814", 215: "N824", 216: "N834", 217: "S804", 218: "S814",
219: "S824", 220: "S834", 221: "E804", 222: "E814", 223: "E824", 224: "E834", 225: "W804", 226: "W814", 227: "W824", 228: "W834", 229: "N808", 230: "N818",
231: "N828", 232: "N838", 233: "S808", 234: "S818", 235: "S828", 236: "S838", 237: "E808", 238: "E818", 239: "E828", 240: "E838", 241: "W808", 242: "W818",
243: "W828", 244: "W838", 245: "E110", 246: "W110", 247: "E120", 248: "W120", 249: "S110", 250: "N110", 251: "S120", 252: "N120", 253: "E111", 254: "W111",
255: "E121", 256: "W121", 257: "S111", 258: "N111", 259: "S121", 260: "N121", 261: "LB01", 262: "LB11", 263: "LB21", 264: "LB31", 265: "LB41", 266: "LB51",
267: "LB61", 268: "LB71", 269: "GB00", 270: "GB10", 271: "GB20", 272: "GB30", 273: "GB40", 274: "GB50", 275: "GB60", 276: "GB70", 277: "VCC", 278: "VSS",
279: "LT00", 280: "LT10", 281: "LT20", 282: "LT30", 283: "LT02", 284: "LT13", 285: "LT01", 286: "LT04", 287: "LBO0", 288: "LBO1", 289: "SS00", 290: "SS40",
291: "GT00", 292: "GT10", 293: "GBO0", 294: "GBO1", 295: "DI0", 296: "DI1", 297: "DI2", 298: "DI3", 299: "DI4", 300: "DI5", 301: "DI6", 302: "DI7",
303: "CIN0", 304: "CIN1", 305: "CIN2", 306: "CIN3", 307: "CIN4", 308: "CIN5", 309: "COUT0", 310: "COUT1", 311: "COUT2", 312: "COUT3", 313: "COUT4", 314: "COUT5"}

with open('dat.json') as f:
    d = json.load(f)

for x in ['X0', 'X1', 'X2', 'X8', 'X11', 'Lut', 'Clk', 'Lsr', 'Ce', 'Sel']:
    print("Wires", x)
    for p, i in zip(d[f'{x}s'], d[f'{x}Ins']): 
        print(nodes.get(p), [nodes.get(n) for n in i])
