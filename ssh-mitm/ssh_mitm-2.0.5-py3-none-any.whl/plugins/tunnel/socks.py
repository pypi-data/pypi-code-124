import logging
import socket
from typing import (
    TYPE_CHECKING,
    List,
    Optional,
    Tuple,
    Union,
    Text
)

import paramiko
from typeguard import typechecked
from rich._emoji_codes import EMOJI
from colored.colored import stylize, fg, attr  # type: ignore

import sshmitm
from sshmitm.forwarders.tunnel import TunnelForwarder, LocalPortForwardingForwarder
from sshmitm.plugins.session.tcpserver import TCPServerThread

from sshmitm.plugins.tunnel.socks4 import Socks4Server, Socks4Error
from sshmitm.plugins.tunnel.socks5 import Socks5Server, Socks5Error

if TYPE_CHECKING:
    from sshmitm.session import Session


class ClientTunnelHandler:
    """
    Similar to the RemotePortForwardingForwarder
    """

    @typechecked
    def __init__(
        self,
        session: 'sshmitm.session.Session'
    ) -> None:
        self.session = session

    @typechecked
    def handle_request(self, listenaddr: Tuple[Text, int], client: Union[socket.socket, paramiko.Channel], addr: Optional[Tuple[str, int]]) -> None:
        if self.session.ssh_client is None or self.session.ssh_client.transport is None:
            return
        destination: Optional[Tuple[Text, int]] = None
        socksconnection: Optional[Union[Socks4Server, Socks5Server]] = None
        try:
            socksversion = client.recv(1)
            if socksversion == Socks4Server.SOCKSVERSION:
                socksconnection = Socks4Server(listenaddr)
                destination = socksconnection.get_address(client, ignore_version=True)
            elif socksversion == Socks5Server.SOCKSVERSION:
                socksconnection = Socks5Server(listenaddr)
                destination = socksconnection.get_address(client, ignore_version=True)
        except (Socks4Error, Socks5Error) as sockserror:
            logging.error('unable to parse SOCKS request! %s', sockserror)
        if destination is None:
            client.close()
            logging.error("unable to parse SOCKS request")
            return
        try:
            logging.debug("Injecting direct-tcpip channel (%s -> %s) to client", addr, destination)
            remote_ch = self.session.ssh_client.transport.open_channel("direct-tcpip", destination, addr)
            TunnelForwarder(client, remote_ch)
        except paramiko.ssh_exception.ChannelException:
            client.close()
            logging.error("Could not setup forward from %s to %s.", addr, destination)


class SOCKSTunnelForwarder(LocalPortForwardingForwarder):
    """Serve out direct-tcpip connections over a session on local ports
    """

    @classmethod
    @typechecked
    def parser_arguments(cls) -> None:
        plugin_group = cls.parser().add_argument_group(cls.__name__)
        plugin_group.add_argument(
            '--socks-listen-address',
            dest='socks_listen_address',
            default='127.0.0.1',
            help='socks server listen address (default: 127.0.0.1)'
        )

    tcpservers: List[TCPServerThread] = []

    # Setup should occur after master channel establishment

    @classmethod
    @typechecked
    def setup(cls, session: 'sshmitm.session.Session') -> None:
        parser_retval = cls.parser().parse_known_args(None, None)
        args, _ = parser_retval

        t = TCPServerThread(
            ClientTunnelHandler(session).handle_request,
            run_status=session.running,
            network=args.socks_listen_address
        )
        t.start()
        cls.tcpservers.append(t)
        logging.info((
            f"{EMOJI['information']} {stylize(session.sessionid, fg('light_blue') + attr('bold'))}"
            f" - local port forwading\n"
            f"{stylize('SOCKS port:', attr('bold'))} {stylize(t.port, fg('light_blue') + attr('bold'))}\n"
            f"  {stylize('SOCKS4:', attr('bold'))}\n"
            f"    * socat: {stylize(f'socat TCP-LISTEN:LISTEN_PORT,fork socks4:127.0.0.1:DESTINATION_ADDR:DESTINATION_PORT,socksport={t.port}', fg('light_blue') + attr('bold'))}\n"
            f"    * netcat: {stylize(f'nc -X 4 -x localhost:{t.port} address port', fg('light_blue') + attr('bold'))}\n"
            f"  {stylize('SOCKS5:', attr('bold'))}\n"
            f"    * netcat: {stylize(f'nc -X 5 -x localhost:{t.port} address port', fg('light_blue') + attr('bold'))}"
        ))
