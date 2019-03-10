// Copyright (C) 2008 Naoyuki Hirayama.
// All Rights Reserved.

// $Id$

#include <iostream>
#include <string>
#include <vector>

using namespace std;

std::vector< std::vector<int> > dd;
void put_dd( int m, int n, int k ) { dd[m][n] = k; }
int get_dd( int m, int n ) { return dd[m][n]; }

int doit( const vector< string >& senames, const vector< string >& queries, int m, int n )
{
        if( n == int( queries.size() ) ) { return 0; }

        if( 0 <= get_dd(m,n) ) {
                return get_dd(m,n);
        }

        if( senames[m] == queries[n] ) {
                int q = INT_MAX;
                for( int k = 0 ; k < int( senames.size() ) ; k++ ) {
                        if( k == m ) { continue; }
                        int p = doit( senames, queries, k, n+1 );
                        if( p < q ) { q = p; }
                }
                put_dd( m, n, q+1 );
                return q+1;
        } else {
                int k = doit( senames, queries, m, n+1 );
                put_dd( m, n, k );
                return k;
        }
}


int doit( const vector< string >& senames, const vector< string >& queries )
{
        int q = INT_MAX;
        for( int k = 0 ; k < int( senames.size() ) ; k++ ) {
                int p = doit( senames, queries, k, 0 );
                if( p < q ) { q = p; }
        }
        return q;
}

int main()
{
        string dummy;

        int N;
        cin >> N;
        for( int i = 0 ; i < N ; i++ ) {
                int S;
                cin >> S;
                getline( cin, dummy );
                //cerr << "S: " << S << endl;

                vector< string > senames;
                for( int j = 0 ; j < S ; j++ ) {
                        string sename;
                        getline( cin, sename );
                        senames.push_back( sename );
                        //cerr << "search engine: " << sename << endl;
                }

                int Q;
                cin >> Q;
                getline( cin, dummy );
                //cerr << "Q: " << Q << endl;

                vector< string > queries;
                for( int j = 0 ; j < Q ; j++ ) {
                        string query;
                        getline( cin, query );
                        queries.push_back( query );

                        //cerr << "query: " << query << endl;
                }

                dd.clear();
                dd.resize( S );
                for( int k = 0 ; k < S ; k++ ) {
                        dd[k].resize( Q );
                        for( int j = 0 ; j < Q; j++ ) {
                                dd[k][j] = -1;
                        }
                }

                cout << "Case #" << ( i+1 ) << ": " << doit( senames, queries ) << endl;
        }


        return 0;
}

