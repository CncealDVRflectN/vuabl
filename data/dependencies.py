from networkx import Graph
import networkx as nx
import utils.conversion as conversion
import utils.theming as theming


def get_dependencies_graph_data(groups: list) -> Graph:
    data: Graph = nx.Graph()

    for group in groups:
        data.add_node(
            f"Group {group.name}", 
            scale=10, 
            size=conversion.bytes_to_readable_size(group.totalSize)
        )

        for archive in group.archives:
            data.add_node(
                f"Archive {archive.name}", 
                scale=5, 
                size=conversion.bytes_to_readable_size(archive.size)
            )

            for explicitAsset in archive.explicitAssets:
                data.add_node(
                    f"Asset {explicitAsset.path}", 
                    scale=1, 
                    size=conversion.bytes_to_readable_size(explicitAsset.totalSize)
                )

            for file in archive.files:
                for dataFromOtherAsset in file.dataFromOtherAssets:
                    data.add_node(
                        f"Asset {dataFromOtherAsset.path}", 
                        scale=1, 
                        size=conversion.bytes_to_readable_size(dataFromOtherAsset.size)
                    )

    colors: list = theming.get_plot_colors()
    colorIndex: int = 0
    colorsCount: int = len(colors)

    for group in groups:
        for archive in group.archives:
            archiveColor = colors[colorIndex % colorsCount]
            colorIndex += 1

            data.add_edge(f"Group {group.name}", f"Archive {archive.name}", color=archiveColor)

            for explicitAsset in archive.explicitAssets:
                data.add_edge(f"Archive {archive.name}", f"Asset {explicitAsset.path}", color=archiveColor)

            for file in archive.files:
                for dataFromOtherAsset in file.dataFromOtherAssets:
                    for referencingAsset in dataFromOtherAsset.referencingAssets:
                        data.add_edge(f"Asset {dataFromOtherAsset.path}", f"Asset {referencingAsset.path}", color=archiveColor)

    return data
