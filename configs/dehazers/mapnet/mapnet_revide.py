_base_ = [
    '../_base_/datasets/revide_video.py',
    '../_base_/default_runtime.py', './map_runtime.py',
    '../_base_/schedules/schedule_80k_eval.py'
]

exp_name = 'mapnet_revide_80k'

checkpoint = 'https://download.openmmlab.com/mmclassification/v0/convnext/downstream/convnext-tiny_3rdparty_32xb128-noema_in1k_20220301-795e9634.pth'  # noqa

# model settings
model = dict(
    type='MAP',
    generator=dict(
        type='MAPNet',
        backbone=dict(
            type='ConvNeXt',
            arch='tiny',
            out_indices=[0, 1, 2, 3],
            drop_path_rate=0.0,
            layer_scale_init_value=1.0,
            gap_before_final_norm=False,
            init_cfg=dict(type='Pretrained', checkpoint=checkpoint, prefix='backbone.'),
        ),
        neck=dict(
            type='ProjectionHead',
            in_channels=[96, 192, 384, 768],
            out_channels=256,
            num_outs=4
        ),
        upsampler=dict(
            type='MAPUpsampler',
            embed_dim=128,
            num_feat=128,
        ),
        channels=128,
        num_trans_bins=32,
        align_depths=(1, 1, 1, 1),
        num_kv_frames=[1, 2],
    ),

    pixel_loss=dict(type='L1Loss', loss_weight=1.0, reduction='mean'),  # L1Loss, CharbonnierLoss
)

data = dict(
    train_dataloader=dict(samples_per_gpu=4, drop_last=True),
)

test_cfg = dict(metrics=['L1', 'PSNR', 'SSIM'], crop_border=0)

# evaluation = dict(interval=400)  # for debug purpose

# runtime settings
work_dir = f'./work_dirs/{exp_name}'
