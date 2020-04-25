#!/bin/bash
function test_python {
    echo "test $1"
    python3 $1
    if [ $? -eq 0 ]; then 
        echo "test passes"
    fi
}

test_python point_test.py
test_python segment_test.py
test_python triangle_test.py
test_python circle_test.py
# # 
test_python e2eTest_ConwayCircle.py
