from pathlib import Path
from modal import App, Image, Volume

app = App("breseq-on-modal")

vol = Volume.from_name("breseq-results", create_if_missing=True)

image = (
    Image.debian_slim()
    .apt_install("wget", "bowtie2", "r-base", "tar")
    .run_commands(
        "wget https://github.com/barricklab/breseq/releases/download/v0.39.0/breseq-0.39.0-Linux-x86_64.tar.gz",
        "tar -xzf breseq-0.39.0-Linux-x86_64.tar.gz",
        "chmod -R 755 breseq-0.39.0-Linux-x86_64",
        "cd breseq-0.39.0-Linux-x86_64 && ./run_tests.sh",
    )
)

CPUs = 64


@app.function(
    image=image, cpu=CPUs, timeout=60 * 60 * 3, volumes={"/root/breseq-results": vol} # Timeout is in seconds
)
def run_breseq(
    reference: Path,
    fastq1: Path,
    fastq2: Path,
):
    from datetime import datetime
    import os

    # Create a new folder in the volume to store the results (should be datetime e.g. 2024-09-10-13:12:00)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    results_dir = f"/root/breseq-results/{timestamp}"
    os.makedirs(results_dir)
    
    vol.commit()
    
    # Run breseq
    import subprocess

    cmd = f"/breseq-0.39.0-Linux-x86_64/bin/breseq -j {CPUs} -r '/root/breseq/{reference}' '/root/breseq/{fastq1}' '/root/breseq/{fastq2}' -o {results_dir}"

    subprocess.run(cmd, shell=True)

    print(f"breseq run finished. Your results can now be retrieved by running:\nmodal volume get breseq-results {timestamp}")

@app.local_entrypoint()
def main():
    import json

    with open("breseq/config.json") as f:
        config = json.load(f)

    run_breseq.remote(
        reference=Path(config["reference"]),
        fastq1=Path(config["fastq1"]),
        fastq2=Path(config["fastq2"]),
    )
