#define MAX_ELEMENTS 100
int score[MAX_ELEMENTS];
int find_max_score(int n) {
    int i, tmp;
    tmp = score[0];

    for(i = 1, i < n; i ++) {
        if(score[i] > tmp) {
            tmp = score[i];
        }
    }
    return tmp;
}