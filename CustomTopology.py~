"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Bandwidth and delay
        bandwidthParameter=100
        delayParameter='500ms'

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch, bw=10, delay='10ms' )
        self.addLink( leftSwitch, rightSwitch, bw=bandwidthParameter, delay=delayParameter )
        self.addLink( rightSwitch, rightHost, bw=10, delay='10ms' )


topos = { 'mytopo': ( lambda: MyTopo() ) }
