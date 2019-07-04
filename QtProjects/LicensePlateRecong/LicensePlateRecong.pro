DISTFILES += \
    ../samples/security_barrier_camera_demo/README.md \
    ../samples/security_barrier_camera_demo/CMakeLists.txt

HEADERS += \
    ../samples/security_barrier_camera_demo/security_barrier_camera.hpp

SOURCES += \
    ../samples/security_barrier_camera_demo/main.cpp
INCLUDEPATH += ../samples/security_barrier_camera_demo/include \
    ../samples/security_barrier_camera_demo/src \
    /data/github_repos/yolov3-tiny-fit-ncs/ncs2/OpenVINO/inference_engine/include \
    /data/github_repos/yolov3-tiny-fit-ncs/ncs2/OpenVINO/inference_engine/samples/common \
    /data/github_repos/yolov3-tiny-fit-ncs/ncs2/OpenVINO/inference_engine/src/extension \
