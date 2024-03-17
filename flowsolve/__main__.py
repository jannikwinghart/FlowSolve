from flowsolve.entity.Flowchart import Flowchart
from flowsolve.entity.nodes.Node import Node
from flowsolve.entity.Edge import Edge
from flowsolve.entity.nodes.IpPortInputNode import IpPortInputNode
from flowsolve.entity.nodes.GetRobotsTxtNode import GetRobotsTxtNode

def main():
    flowchart = Flowchart(
        id=1,
        title="Flowchart 1",
        description="This is the first flowchart"
    )

    ip_port_node = IpPortInputNode(
        id=0,
        title="Check for Open HTTP Port",
        description="Check for an open HTTP port on the target system and enter the address",
        inputs={},
    )

    robots_txt_node = GetRobotsTxtNode(
        id=1,
        title="Get robots.txt",
        description="Get the robots.txt file from a specified IP address and port",
        inputs={"ip": ip_port_node.outputs["ip"], "port": ip_port_node.outputs["port"]},
    )

    edge1 = Edge(
        id=1,
        title="Edge 1",
        description="This is the first edge",
        start_node=ip_port_node,
        end_node=robots_txt_node,
        conditions=[],
        parameters={"ip": "ip", "port": "port"},
    )

    flowchart.addNode(ip_port_node)
    flowchart.addNode(robots_txt_node)
    flowchart.addEdge(edge1)

    ip_port_node.trigger()

    flowchart.run()

    print(flowchart)

if __name__ == "__main__":
    main()
