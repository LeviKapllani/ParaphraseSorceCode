#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#define sqr(x) ((x)*(x))

using namespace std;

int list[2][100];

int main()
{
    int N;
    cin >> N;
    for(int cccccc=0;cccccc < N;++cccccc)
    {
        cout << "Case #" << cccccc+1 << ": ";

        // CODE
        memset(list, 0, sizeof(list));
        int len;
        cin >> len;
        vector<string> engines;
        string str;
        getline(cin, str);
        for(int i=0;i<len;++i)
        {
            getline(cin, str);
            engines.push_back(str);
        }
        cin >> len;
        getline(cin, str);
        int now = 0;
        if (len == 0) {cout << "0" << endl; continue;}
        for (int i=0;i<len;++i)
        {
            getline(cin, str);
            for (int j=0;j<engines.size();++j)
            {
                if (str != engines[j])
                {
                    list[1-now][j] = list[now][j];
                }
                else
                {
                    int mini = 1000000;
                    for(int k=0;k<engines.size();++k)
                    {
                        if (engines[k] != str && mini > list[now][k])
                        {
                            mini = list[now][k];
                        }
                    }
                    list[1-now][j] = mini + 1;
                }
            }
            now = 1-now;
        }
        int mini = -1;
        for (int i=0;i<engines.size();++i)
        {
            if (list[now][i] >= 0 && (mini < 0 || mini > list[now][i]))
            {
                mini = list[now][i];
            }
        }
        
        cout << mini << endl;
        // END OF CODE
    }
    return 0;
}