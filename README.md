# Cloud-based breseq
Runs breseq in the cloud, no fast computer necessary.

## How to run breseq

### Log in to modal
1. Sign up to [modal.com](https://modal.com/signup)
2. Follow the modal quickstart guide:
    ```
    pip install modal
    python3 -m modal setup
    ```
3. Clone this repository to your computer: `git clone `
4. Place your fastq files (can be zipped or unzipped) into the `breseq` folder.
5. Edit the `config.json` to correctly name the fastq and reference sequence.