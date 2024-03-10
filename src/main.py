from entity.Flowchart import Flowchart
from entity.Node import Node
from entity.Edge import Edge
from entity.actions.IpPortInputAction import IpPortInputAction
from entity.actions.GetSitemapAction import GetSitemapAction

def main():
    flowchart = Flowchart(
        id=1,
        title="Flowchart 1",
        description="This is the first flowchart"
    )

    ip_port_input_action = IpPortInputAction(
        id=0,
        title="IP Port Input Action",
        description="This action is used to input an IP address and a port"
    )

    ip_port_node = Node(
        id=0,
        title="Check for Open HTTP Port",
        description="Check for an open HTTP port on the target system and enter the address",
        inputs={},
        actions={"ip_port": ip_port_input_action},
    )

    get_sitemap_action = GetSitemapAction(
        id=1,
        title="Get Sitemap Action",
        description="This action is used to get the sitemap.xml file from the target system"
    )

    sitemap_node = Node(
        id=1,
        title="Get sitemap.xml",
        description="Get the sitemap.xml file from a specified IP address and port",
        inputs={"ip": ip_port_node.outputs["ip_port"]["ip"], "port": ip_port_node.outputs["ip_port"]["port"]},
        actions={"sitemap": get_sitemap_action},
    )

    edge1 = Edge(
        id=1,
        title="Edge 1",
        description="This is the first edge",
        startNode=ip_port_node,
        endNode=sitemap_node,
        conditions=[]
    )

    flowchart.addNode(ip_port_node)
    flowchart.addNode(sitemap_node)
    flowchart.addEdge(edge1)

    flowchart.run()

    print(flowchart)

if __name__ == "__main__":
    main()
