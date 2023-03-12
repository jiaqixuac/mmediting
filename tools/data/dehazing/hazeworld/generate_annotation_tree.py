"""
The code to generate annotation trees,
which can help video frame loading.
"""
import argparse
import os
import os.path as osp
import json
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', default='./data/HazeWorld',
                        help='the folder path to the dataset')
    parser.add_argument('--split', help='train or val or debug or test')
    parser.add_argument('--annotation-name', default='meta_info_tree_GT_{}.json')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    root = args.data_root
    split = args.split
    split = 'test' if split in ('val', 'debug') else split
    assert osp.isdir(root)

    datasets = os.listdir(osp.join(root, split, 'gt'))
    print(f"\n[HazeWorld-{split}]\tDatasets ({len(datasets)}): {datasets}\n")

    data_infos = {}
    lines = []
    bar = tqdm(datasets)
    for dataset in bar:
        folders = os.listdir(osp.join(root, split, 'gt', dataset))
        folders.sort()

        if args.split in ('val', 'debug'):
            num = int(len(folders) / 4)  # 4: 4 betas
            step = int(num / 5) * 4
            folders = folders[::step] + folders[1::step] + folders[2::step] + folders[3::step]
            folders.sort()
            folders = folders[:20] if args.split == 'val' else folders[:1]  # 20 for val, and 1 for debug

        for folder in folders:
            clip_name = osp.join(dataset, folder)
            bar.set_description(f"[{clip_name}]")
            assert osp.exists(osp.join(root, split, 'hazy', dataset, folder))

            files = os.listdir(osp.join(root, split, 'gt', dataset, folder))

            files.sort()
            assert len(files) == len(os.listdir(osp.join(root, split, 'hazy', dataset, folder)))
            data_infos[clip_name] = []
            for file in files:
                gt_path = osp.join(root, split, 'gt', dataset, folder, file)
                hazy_path = osp.join(root, split, 'hazy', dataset, folder, file)
                assert osp.exists(gt_path) and osp.exists(hazy_path)
                data_infos[clip_name].append(str(file))
                lines.append(f"{osp.join(dataset, folder, file)}\n")

    print(f"\n[{args.split}] {len(lines)}\n")
    os.makedirs(osp.join(root, split), exist_ok=True)
    annotation_name = args.annotation_name.format(split)
    with open(osp.join(root, split, annotation_name), 'w') as f:
        json.dump(data_infos, f)
