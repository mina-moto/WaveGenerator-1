import platform
import os

# Network config
# Input width and Height
Width = 120
Channel = 1

# Data augmentation
Data_range = (0, 100)
Outlier = True
Normalize = True
Zero_Exclusion = True

#File_extensions = ['.jpg', '.png']

# Training config
Iteration = 5000
Minibatch = 16
# 5000iteration = 30epoch (Minibatch 16 * 19)

# Test config
# The total number of generated images is Test_Minibatch * Test_num
Test_Minibatch = 16  # 100
Test_num = 10
Save_test_img_dir = 'test'

# if Save_combine is True, generated images in test are stored combined with same minibatch's
# if False, generated images are stored separately
# if None, generated image is not stored
Save_train_combine = True
Save_test_combine = True

Save_train_step = 100
Save_iteration_disp = True

# Save config
Save_dir = 'models'
Save_d_name = 'D.h5'
Save_g_name = 'G.h5'
Save_d_path = os.path.join(Save_dir, Save_d_name)
Save_g_path = os.path.join(Save_dir, Save_g_name)
Save_train_img_dir = 'train'
Save_img_num = 5

# Other config
# Randon_seed is used for seed of dataset shuffle in data_loader.py
Random_seed = 0

# Check
#variety = ['channels_first', 'channels_last']
# if not Input_type in variety:
#raise Exception("unvalid Input_type")

#os.system("rm {}/*".format(Save_train_img_dir))
python_version = int(platform.python_version_tuple()[0])
if python_version == 3:
    os.makedirs(Save_dir, exist_ok=True)
    os.makedirs(Save_train_img_dir, exist_ok=True)
    os.makedirs(Save_test_img_dir, exist_ok=True)
elif python_version == 2:
    if not os.path.exists(Save_dir):
        os.makedirs(Save_dir)
    if not os.path.exists(Save_train_img_dir):
        os.makedirs(Save_train_img_dir)
    if not os.path.exists(Save_test_img_dir):
        os.makedirs(Save_test_img_dir)
