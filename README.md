# Cloud-based breseq
Runs breseq in the cloud, no fast computer necessary.

## How to run breseq

### 1. Log in to modal
1. Sign up to [modal.com](https://modal.com/signup)
2. Follow the modal quickstart guide:
    ```
    pip install modal
    python3 -m modal setup
    ```
### 2. Repository and file setup
3. Clone this repository to your computer: `git clone https://github.com/tdsone/breseq-on-modal.git`
4. Place your fastq files (can be zipped or unzipped) into the `breseq` folder.
5. Edit the `config.json` to correctly name the fastq and reference sequence.
### 3. Running breseq and retrieving results
6. Open a terminal and make sure you are in the root folder of this repository. To check if you are in the right folder, run `pwd`. This should show `<blablabla>/breseq-on-modal` but e.g. not `<blablabla>/breseq-on-modal/breseq`.
7. Now, in your terminal, run `modal run --detach breseq.main` to run breseq. This will take a while (up to an hour).
8. You can always check the status of the run in the ephemeral apps tab: 
    ![alt text](image.png)
9.  Once it's done, you have to download the files: `modal volume get breseq-results`