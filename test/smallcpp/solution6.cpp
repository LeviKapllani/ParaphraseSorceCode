#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>


using namespace std;

int s;
int q;

map <string, int> engines;
vector <int> queries;
vector <vector<int>> cost;

void input()
{
	engines.clear();
	queries.clear();

	char buffer[101];
	cin>>s;
	cin.getline(buffer, 101);
	for (int i = 0; i < s; i++) {
		cin.getline(buffer, 101);
		string temp(buffer);
		engines[temp] = i;
	}

	cin>>q;
	cin.getline(buffer, 101);
	for (int i = 0; i < q; i++) {
		cin.getline(buffer, 101);
		string temp(buffer);
		int key = engines.find(temp)->second;
		queries.push_back(key);
	}
	return;
}

int dp()
{
	cost.clear();
	cost = vector< vector<int> >(q, s);

	for (int i = 0; i < s; i++) {
		cost[q - 1][i] = 0;
	}
	cost[q-1][queries[q - 1]] = 1;

	for (int i = q - 2; i >= 0; i--) {
		for (int j = 0; j < s; j++) {
			int min = 0x7fffffff;
			int key = queries[i];
			int value = 0;
			for (int k = 0; k < s; k++) {
				if (key != k) {
					if (j == k) {
						value = cost[i+1][j];
					} else {
						value = cost[i+1][k] + 1;
					}
				} else {
					continue;
				}
				if (value < min) {
					min = value;
				}
			}
			cost[i][j] = min;
		}
	}

	int min = 0x7ffffff;
	for (int i = 0; i < s; i++) {
		if (cost[0][i] < min) {
			min = cost[0][i];
		}
	}
	return min;
}

int main()
{
	int n;
	int result = 0;

	cin>>n;
	for (int i = 0; i < n; i++) {
		input();
		if (q == 0 || q == 1) {
			result = 0;
		} else {
			result = dp();
		}
		cout<<"Case #"<<i + 1<<": "<<result<<endl;
	}
	return 0;
}
