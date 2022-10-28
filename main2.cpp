#include <iostream>
using namespace std;

struct Point{
    double x;
    double y;
    Point(){ //default starting value
        x = 0;
        y = 0;
    }
    Point(double x, double y){
        this->x = x;
        this->y = y;
    }
    ~Point(){
        cout << "Point destroyed" << endl;
    }
    void output(){
        cout << "OUTPUT X AND Y COORDINATES OF A POINT" << endl;
        cout << "x = " << x << "; y = " << y << endl;
    }
};
int main()
{
    Point* A = new Point();
    cout << "Created new point A" << endl;
    //delete A;
    Point B(3.2, 5.4);
    cout << "Created new point B" << endl;
    B.output();
    return 0;
}
