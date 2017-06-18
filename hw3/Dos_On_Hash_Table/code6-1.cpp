#include <iostream>
#include <unordered_map>
#include <fstream>
using namespace std;

int main()
{
    ofstream output_file("input6-1.txt");
    unordered_map<int, int> ht;

    int bucket_size = ht.bucket_count();
    int total_num = 50000;

    output_file << total_num << "\n";
    int num = 0;
    int i = 1;
    while(true)
    {
        int value = i * ht.bucket_count();
        ht[value] = i;
        int nbuckets = ht.bucket_count();
        output_file << value << "\n";
        num++;
        i++;
        if(bucket_size != ht.bucket_count()){
            bucket_size = ht.bucket_count();
            i = 1;
        }
        if(num > total_num)
        {
            break;
        }

    }
    output_file.close();
    return 0;
}
