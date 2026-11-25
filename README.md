# Emir Cabalak

Final-year AI Engineering student (OSTİM Technical University, Erasmus+ at Riga Technical University).
I build ML models and then try to break my own results: leakage checks, grouped splits, honest baselines,
and negative results reported alongside the positive ones.

## Work worth reading

**[adaptive-traffic-forecasting](https://github.com/emircabalak/adaptive-traffic-forecasting)**: online adaptation of a Graph WaveNet traffic forecaster during sudden disruptions.
- Reproduces the paper (test MAE 2.70 / 3.10 / 3.53 vs. reported 2.69 / 3.07 / 3.53).
- An error decomposition shows at most 18% of the 60-minute error is reachable by *any* online update. A per-sensor adapter improves disrupted-period MAE without hurting normal periods. Naive fine-tuning makes things 3.4 mph worse.
- 27 pre-registered experiments in [`docs/EXPERIMENTS.md`](https://github.com/emircabalak/adaptive-traffic-forecasting/blob/main/docs/EXPERIMENTS.md).

**[flyrank-ml-internship](https://github.com/emircabalak/flyrank-ml-internship)**: ranking which pages editors should refresh first (FlyRank internship, anonymized search data).
- Client-grouped CV on 30k pages / 32 clients. Precision@50 is 0.81 vs. 0.66 for the strongest rule baseline (base rate 0.60).
- Leakage ablation: AUC climbs from 0.63 (honest) to 0.95 and then 0.997 as leaky windows are added.

**[uncertainty-aware-3d-detection](https://github.com/emircabalak/uncertainty-aware-3d-detection)**: evidential uncertainty for LiDAR 3D detection on KITTI.
- Swapping in a pretrained backbone raises mAP from 37% to 55%, but the uncertainty signal stops separating true from false positives (AUROC 0.69 → ~0.50).

**[emircabalak.github.io](https://emircabalak.github.io)**: write-ups on evaluation mistakes, plus an in-browser leakage checker.

## Contact
[LinkedIn](https://www.linkedin.com/in/emircabalak/) · [Site](https://emircabalak.github.io)
