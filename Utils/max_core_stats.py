import os
import sys
import csv
import networkx as nx
import argparse
from multiprocessing import Pool, cpu_count

# Hardcoded list of graph filenames to process
# SELECTED_FILES = [
# "176bit_LCC_remapped",
# "3D_28984_Tetra_LCC_remapped",
# "598a_LCC_remapped",
# "AIDS_LCC_remapped",
# "CA-CondMat_cleaned_LCC_remapped",
# "CA-HepTh_cleaned_LCC_remapped",
# "CL-10K-1d8-L5_LCC_remapped",
# "OHSU_LCC_remapped",
# "as20000102_cleaned_LCC_remapped",
# "bio-grid-fruitfly_LCC_remapped",
# "bio-grid-human_LCC_remapped",
# "ca-CondMat_LCC_remapped",
# "ca-MathSciNet_LCC_remapped",
# "cit-DBLP_LCC_remapped",
# "com-amazon_ungraph_cleaned_LCC_remapped",
# "econ-poli-large_LCC_remapped",
# "email-EU_LCC_remapped",
# "escorts_LCC_remapped",
# "ia-dbpedia-team-bi_LCC_remapped",
# "ia-email-EU_LCC_remapped",
# "ia-escorts-dynamic_LCC_remapped",
# "oregon1_010331_cleaned_LCC_remapped",
# "oregon1_010407_cleaned_LCC_remapped",
# "oregon1_010526_cleaned_LCC_remapped",
# "out_dimacs10-as22july06_cleaned_LCC_remapped",
# "out_dimacs10-cond-mat-2003_cleaned_LCC_remapped",
# "out_douban_cleaned_LCC_remapped",
# "out_petster-hamster_cleaned_LCC_remapped",
# "out_sociopatterns-infectious_cleaned_LCC_remapped",
# "soc-political-retweet_LCC_remapped",
# ]

SELECTED_FILES = [
# "BZR_LCC_remapped",
# "COIL-RAG_LCC_remapped",
# "COX2_LCC_remapped",
# "DBLP-v1_LCC_remapped",
# "DD_LCC_remapped",
# "DD_g1061_LCC_remapped",
# "DD_g205_LCC_remapped",
# "DD_g220_LCC_remapped",
# "DD_g223_LCC_remapped",
# "DD_g231_LCC_remapped",
# "DD_g251_LCC_remapped",
# "DD_g31_LCC_remapped",
# "DD_g338_LCC_remapped",
# "DD_g433_LCC_remapped",
# "DD_g441_LCC_remapped",
# "DD_g476_LCC_remapped",
# "DD_g485_LCC_remapped",
# "DD_g505_LCC_remapped",
# "DD_g508_LCC_remapped",
# "DD_g55_LCC_remapped",
# "DD_g564_LCC_remapped",
# "DD_g597_LCC_remapped",
# "DD_g59_LCC_remapped",
# "DD_g601_LCC_remapped",
# "DD_g623_LCC_remapped",
# "DD_g641_LCC_remapped",
# "DD_g656_LCC_remapped",
# "DD_g669_LCC_remapped",
# "DD_g687_LCC_remapped",
# "DD_g68_LCC_remapped",
# "DD_g709_LCC_remapped",
# "DD_g721_LCC_remapped",
# "DD_g736_LCC_remapped",
# "DD_g752_LCC_remapped",
# "DD_g793_LCC_remapped",
# "DD_g877_LCC_remapped",
# "DD_g884_LCC_remapped",
# "DD_g93_LCC_remapped",
# "DD_g94_LCC_remapped",
# "DD_g95_LCC_remapped",
# "DHFR_LCC_remapped",
# "ENZYMES_LCC_remapped",
# "FRANKENSTEIN_LCC_remapped",
# "Fingerprint_LCC_remapped",
# "Letter-high_LCC_remapped",
# "MSRC-21C_LCC_remapped",
# "Mutag_LCC_remapped",
# "SW-10000-6-0d3-L5_LCC_remapped",
# "SYNTHETIC_LCC_remapped",
# "Synthie_LCC_remapped",
# "cleaned_144_LCC_remapped",
# "cleaned_KKI_LCC_remapped",
# "cleaned_Peking-1_LCC_remapped",
# "cleaned_TerroristRel_LCC_remapped",
# "cleaned_auto_LCC_remapped",
# "cleaned_bio-dmela_LCC_remapped",
# "cleaned_bio-grid-plant_LCC_remapped",
# "cleaned_c-fat200-1_LCC_remapped",
# "cleaned_c-fat500-1_LCC_remapped",
# "cleaned_channel-500x100x100-b050_LCC_remapped",
# "cleaned_citationCiteseer_LCC_remapped",
# "cleaned_eco-florida_LCC_remapped",
# "cleaned_eco-foodweb-baydry_LCC_remapped",
# "cleaned_eco-mangwet_LCC_remapped",
# "cleaned_email-univ_LCC_remapped",
# "cleaned_hamming6-4_LCC_remapped",
# "cleaned_ia-fb-messages_LCC_remapped",
# "cleaned_inf-USAir97_LCC_remapped",
# "cleaned_infect-dublin_LCC_remapped",
# "cleaned_infect-hyper_LCC_remapped",
# "cleaned_m14b_LCC_remapped",
# "cleaned_rgg_n_2_15_s0_LCC_remapped",
# "cleaned_rgg_n_2_16_s0_LCC_remapped",
# "cleaned_rgg_n_2_17_s0_LCC_remapped",
# "cleaned_rgg_n_2_18_s0_LCC_remapped",
# "cleaned_rgg_n_2_19_s0_LCC_remapped",
# "cleaned_rgg_n_2_20_s0_LCC_remapped",
# "cleaned_rgg_n_2_21_s0_LCC_remapped",
# "cleaned_tech-caidaRouterLevel_LCC_remapped",
# "cleaned_venturiLevel3_LCC_remapped",
# "cop20k_A_LCC_remapped",
# "out_cleaned_edit-itwikinews_LCC_remapped",
# "out_dimacs10-cond-mat-2005_cleaned_LCC_remapped",
# "roadNet-CA_cleaned_LCC_remapped",
# "roadNet-PA_cleaned_LCC_remapped",
# "roadNet-TX_cleaned_LCC_remapped",

"as19971108_remapped",
"as19991006_remapped",
"as19991007_remapped",
"as19991008_remapped",
"as19991009_remapped",
"as19991010_remapped",
"as19991011_remapped",
"as19991013_remapped",
"as19991016_remapped",
"as19991017_remapped",
"as19991018_remapped",
"as19991019_remapped",
"as19991026_remapped",
"as19991027_remapped",
"as19991028_remapped",
"as19991031_remapped",
"as19991105_remapped",
"as19991108_remapped",
"as19991111_remapped",
"as19991113_remapped",
"as19991114_remapped",
"as19991115_remapped",
"as19991116_remapped",
"as19991118_remapped",
"as19991121_remapped",
"as19991122_remapped",
"as19991204_remapped",
"as19991205_remapped",
"as19991206_remapped",
"as20000102_remapped",

]


# Maximum number of files to process per batch

BATCH_SIZE = 3  # Max files per batch

# ------------------- Graph Reader -------------------
def read_grh(file_path):
    G = nx.Graph()
    with open(file_path, "r") as f:
        for u, line in enumerate(f):
            parts = line.strip().split()
            if not parts:
                continue
            neighbors = map(int, parts)
            for v in neighbors:
                G.add_edge(u, v)

    # Remove any accidental self-loops
    G.remove_edges_from(nx.selfloop_edges(G))
    return G


# ------------------- Max Core Processor -------------------
def process_file(file_path):
    """
    Process a single .grh file and return stats for its max core.
    """
    try:
        G = read_grh(file_path)

        # Compute core numbers
        core_numbers = nx.core_number(G)
        max_core_num = max(core_numbers.values(), default=0)

        # Extract max-core subgraph
        max_core_nodes = [n for n, k in core_numbers.items() if k == max_core_num]
        max_core_subgraph = G.subgraph(max_core_nodes).copy()

        # Compute stats
        mxc_nodes = max_core_subgraph.number_of_nodes()
        mxc_edges = max_core_subgraph.number_of_edges()
        mxc_density = nx.density(max_core_subgraph)
        mxc_max_degree = max(dict(max_core_subgraph.degree()).values(), default=0)
        mxc_avg_degree = (
            sum(dict(max_core_subgraph.degree()).values()) / mxc_nodes
            if mxc_nodes > 0 else 0
        )

        return [
            os.path.splitext(os.path.basename(file_path))[0],
            max_core_num,
            mxc_nodes,
            mxc_edges,
            round(mxc_density, 6),
            mxc_max_degree,
            round(mxc_avg_degree, 6)
        ]

    except Exception as e:
        return [os.path.basename(file_path), "ERROR", "", "", "", "", str(e)]

# ------------------- Helper -------------------
def chunked_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# ------------------- Main -------------------
def main(folder_path, num_cpus):
    graph_files = []
    for name in SELECTED_FILES:
        file_path = os.path.join(folder_path, f"{name}.grh")
        if os.path.isfile(file_path):
            graph_files.append(file_path)

    if not graph_files:
        print("No matching .grh files found in folder.")
        return

    print("\nFiles to process:")
    for f in graph_files:
        print(f"  - {os.path.basename(f)}")
    print(f"\nTotal {len(graph_files)} files to process.")
    print(f"Using {num_cpus} CPUs with batch size {BATCH_SIZE}.")

    all_results = []

    # Process files in batches
    for batch_num, batch in enumerate(chunked_list(graph_files, BATCH_SIZE), start=1):
        print(f"\nProcessing batch {batch_num}: {len(batch)} files...")
        with Pool(processes=num_cpus) as pool:
            for result in pool.imap(process_file, batch):
                all_results.append(result)

    # Write results to CSV
    output_file = "real_max_core_stats_21-10-25.csv"
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "graph_file", "mxc_core", "mxc_nodes",
            "mxc_edges", "mxc_density",
            "mxc_max_degree", "mxc_avg_degree"
        ])
        writer.writerows(all_results)

    print(f"\nAll batches completed. Results saved to {output_file}")

# ------------------- Entry Point -------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process GRH graph files for max core stats")
    parser.add_argument("--input", required=True, help="Path to folder containing .grh files")
    parser.add_argument("--cpu", type=int, default=min(10, max(1, cpu_count())), help="Max number of CPUs to use")
    args = parser.parse_args()

    main(args.input, args.cpu)


