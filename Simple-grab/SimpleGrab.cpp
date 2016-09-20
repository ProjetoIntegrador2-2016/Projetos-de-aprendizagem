//g++ $(pkg-config --libs --cflags opencv) -o program program.cpp
#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char **argv){

	VideoCapture cap(0);

	if(!cap.isOpened()){
		cerr << "Error: Unable to open the camera"<< endl;
		return 0;
	}

	Mat frame;
	cout << "Start grabing , press any key on Live window to terminate" << endl;
	
	while(1){
		cap >> frame;
		if(frame.empty()){
			cerr << "Error: Unable to grab camera" << endl;
			break;
		}
		imshow("Live",frame);
		if(waitKey(1)>=0){
			break;
		}

	}

	cout << "Closing the camera" << endl;
	cap.release();
	destroyAllWindows();
	cout << "bye" << endl;
	return 0;

}
