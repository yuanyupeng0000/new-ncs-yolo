DISTFILES += \
    ../samples/human_pose_estimation_demo/README.md \
    ../samples/human_pose_estimation_demo/CMakeLists.txt

HEADERS += \
    ../samples/human_pose_estimation_demo/include/human_pose.hpp \
    ../samples/human_pose_estimation_demo/include/human_pose_estimation_demo.hpp \
    ../samples/human_pose_estimation_demo/include/human_pose_estimator.hpp \
    ../samples/human_pose_estimation_demo/include/peak.hpp \
    ../samples/human_pose_estimation_demo/include/render_human_pose.hpp

SOURCES += \
    ../samples/human_pose_estimation_demo/src/human_pose.cpp \
    ../samples/human_pose_estimation_demo/src/human_pose_estimator.cpp \
    ../samples/human_pose_estimation_demo/src/peak.cpp \
    ../samples/human_pose_estimation_demo/src/render_human_pose.cpp \
    ../samples/human_pose_estimation_demo/main.cpp
INCLUDEPATH += ../samples/human_pose_estimation_demo/include \
    ../samples/human_pose_estimation_demo/src \
    /data/github_repos/yolov3-tiny-fit-ncs/ncs2/OpenVINO/inference_engine/include \
    /data/github_repos/yolov3-tiny-fit-ncs/ncs2/OpenVINO/inference_engine/samples/common/
