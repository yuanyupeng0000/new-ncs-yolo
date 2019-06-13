new_dir=$1
if [ "$new_dir" = "" ]; then
  echo "new dir empty, please input new dir"
  exit 1
fi
sudo cp -r /media/yyp/DATA/Public_Datasets/ZENITH_DATASETS/empty_structure_VOCdevkit /media/yyp/DATA/Public_Datasets/ZENITH_DATASETS/VOCdevkit_$new_dir
sudo mkdir /media/yyp/DATA/Public_Datasets/ZENITH_DATASETS/VOCdevkit_$new_dir/VOC2007/temp_images/
sudo mkdir -p /media/yyp/DATA/Public_Datasets/ZENITH_DATASETS/VOCdevkit_$new_dir/VOC2007/temp_xmls/
echo /media/yyp/DATA/Public_Datasets/ZENITH_DATASETS/VOCdevkit_$new_dir/VOC2007/temp_images/
echo /media/yyp/DATA/Public_Datasets/ZENITH_DATASETS/VOCdevkit_$new_dir/VOC2007/temp_xmls/
