#define _CRT_SECURE_NO_DEPRECATE

#include<algorithm>

#include<cstdio>

#include<cstdlib>

#include<iostream>

#include<sstream>

#include<fstream>

#include<map>

#include<vector>

#include<cmath>

using namespace std;


const int maxQ = 2001;

const int maxS = 201;

const int inf = (int) 2e9;

int testcases;

int Q, S;

string name[maxS];

map<string, int> index;

int Query[maxQ];


int F[maxS], oldmin, nowmin;

int main() {

    ifstream cin("A.in");

	ofstream cout("A.out");

	cin >> testcases;

	for (int cases = 1; cases <= testcases; cases++) {

		cin >> S;

		index.clear();

		for (int i = 1; i <= S; i++) { 
			
			getline(cin, name[i]); 

			if (i == 1) getline(cin, name[i]);
			
			index[name[i]] = i; 
		}

		cin >> Q;

		for (int i = 1; i <= Q; i++) {

			string tmp;

			getline(cin, tmp);

			if (i == 1) getline(cin, tmp);

			if (index.find(tmp) == index.end()) cout << "Error occur "<< endl;

			Query[i] = index[tmp];
		}

		memset(F, 0, sizeof F);

		oldmin = 0;

		for (int i = 1; i <= Q; i++) {

			nowmin = inf;

			for (int k = 1; k <= S; k++) if (Query[i] != k) {

				if (oldmin + 1 < F[k]) F[k] = oldmin + 1;

				if (F[k] < nowmin) nowmin = F[k];
			}

			F[Query[i]] = inf;

//			cout << "line i " ;

//			for (int k = 1; k <= S; k++) cout << F[k] << " ";

//			cout << "nowmin = " << nowmin << endl;

			oldmin = nowmin;
		}

		cout << "Case #" << cases << ": " << nowmin << endl;
	}

	return 0;
}
