import numpy as np  
import sys,os  
caffe_root = '/data/ssd-caffe/cp_caffe/'
sys.path.insert(0, caffe_root + 'python')  
import caffe  

train_proto = 'yolov3-tiny-ncs-without-last-maxpool.prototxt'
#train_model = 'snapshot/mobilenet_iter_7000.caffemodel'  #should be your snapshot caffemodel

if(len(sys.argv) < 2):
    print("please input caffemodel file from commandLine")
    exit(1)
train_model = sys.argv[1]

deploy_proto = 'yolov3-tiny-ncs-without-last-maxpool-merg-batchnorm.prototxt'  
#save_model = 'iter_7000_MobileNetSSD_deploy.caffemodel'
save_model = train_model.split('/')[-1] + "MobileNetSSD_deploy.caffemodel"

def merge_bn(net, nob):
    '''
    merge the batchnorm, scale layer weights to the conv layer, to  improve the performance
    var = var + scaleFacotr
    rstd = 1. / sqrt(var + eps)
    w = w * rstd * scale
    b = (b - mean) * rstd * scale + shift
    '''
    for key in net.params.iterkeys():
        print("key:" + str(key))
        if type(net.params[key]) is caffe._caffe.BlobVec:
            print("is caffe._caffe.BlobVec")
            if key.endswith("-bn") or key.endswith("-scale"):
                continue
            else:
                conv = net.params[key]
                print("merge layer {0}".format(conv))
                if not net.params.has_key(key + "-bn"):
                    print("not need bn")
                    for i, w in enumerate(conv):
                        nob.params[key][i].data[...] = w.data
                else:
                    bn = net.params[key + "-bn"]
                    scale = net.params[key + "-scale"]
                    wt = conv[0].data
                    channels = wt.shape[0]
                    bias = np.zeros(wt.shape[0])
                    if len(conv) > 1:
                        bias = conv[1].data
                    mean = bn[0].data
                    var = bn[1].data
                    scalef = bn[2].data

                    scales = scale[0].data
                    shift = scale[1].data

                    if scalef != 0:
                        scalef = 1. / scalef
                    mean = mean * scalef
                    var = var * scalef
                    rstd = 1. / np.sqrt(var + 1e-5)
                    rstd1 = rstd.reshape((channels,1,1,1))
                    scales1 = scales.reshape((channels,1,1,1))
                    wt = wt * rstd1 * scales1
                    bias = (bias - mean) * rstd * scales + shift
                    
                    nob.params[key][0].data[...] = wt
                    nob.params[key][1].data[...] = bias

net = caffe.Net(train_proto, train_model, caffe.TRAIN)  
net_deploy = caffe.Net(deploy_proto, caffe.TEST)  

merge_bn(net, net_deploy)
net_deploy.save(save_model)

