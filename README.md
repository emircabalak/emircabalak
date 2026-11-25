# Emir Cabalak

Final-year AI Engineering student (OSTİM Technical University, Erasmus+ at Riga Technical University).
I build ML models and then try to break my own results: leakage checks, grouped splits, honest baselines,
and negative results reported alongside the positive ones.

## Work worth reading

**[adaptive-traffic-forecasting](https://github.com/emircabalak/adaptive-traffic-forecasting)**: online adaptation of a Graph WaveNet traffic forecaster during sudden disruptions.
- Reproduces the paper (test MAE 2.70 / 3.10 / 3.53 vs. reported 2.69 / 3.07 / 3.53).
- An error decomposition shows at most 18% of the 60-minute error is reachable by *any* online update. Naive fine-tuning makes things 3.4 mph worse.
- My learned per-sensor adapter helps, with a CI that excludes zero, but a 3-line EWMA bias correction matches it (paired difference CI includes zero). I reported that too.
- 27 pre-registered experiments in [`docs/EXPERIMENTS.md`](https://github.com/emircabalak/adaptive-traffic-forecasting/blob/main/docs/EXPERIMENTS.md).

**[flyrank-ml-internship](https://github.com/emircabalak/flyrank-ml-internship)**: ranking which pages editors should refresh first (FlyRank internship, anonymized search data).
- Client-grouped CV on 30k pages / 32 clients. Precision@50 is 0.81 vs. 0.66 for the strongest rule baseline (base rate 0.60).
- Then I tried to break it. A 3-column model of last month's traffic matches the full model's AUC (0.623 vs 0.627), so most of the skill is regression to the mean, not content signals.

**[uncertainty-aware-3d-detection](https://github.com/emircabalak/uncertainty-aware-3d-detection)**: evidential uncertainty for LiDAR 3D detection on KITTI.
- Swapping in a pretrained backbone raises mAP from 37% to 55%, but the uncertainty signal stops separating true from false positives (AUROC 0.69 → ~0.50).

**[emircabalak.github.io](https://emircabalak.github.io)**: write-ups on evaluation mistakes, plus an in-browser leakage checker.

## Contact
[LinkedIn](https://www.linkedin.com/in/emircabalak/) · [Site](https://emircabalak.github.io)
