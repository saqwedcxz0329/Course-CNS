#include <iostream>
#include <unordered_map>
#include <fstream>
using namespace std;
int main() {
    unordered_map<int, int> ht;
    string line;
    ifstream inputFile;
    inputFile.open("./input6-1.txt");
    if (inputFile.is_open())
    {   
        int value = 0;
        getline (inputFile,line);
        while ( getline (inputFile,line) )
        {   
            // cout << value << '\n';
            int index = stoi(line);
            ht[index] = value;
            value++;
        }
        inputFile.close();
    }

    cout << "Bucket number: " << ht.bucket_count() << endl;
    return 0;
}
