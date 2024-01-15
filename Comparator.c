#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Player structure
struct Player {
    char name[100];
    int score;
};

// Comparator function for sorting
int compare(const void *a, const void *b) {
    struct Player *playerA = (struct Player *)a;
    struct Player *playerB = (struct Player *)b;

    // Sort descending by score
    if (playerA->score != playerB->score) {
        return playerB->score - playerA->score;
    }
    // Sort ascending by name if scores are the same
    else {
        return strcmp(playerA->name, playerB->name);
    }
}

int main() {
    int n;
    scanf("%d", &n);

    // Create an array of Player structures
    struct Player players[n];

    // Input player data
    for (int i = 0; i < n; i++) {
        scanf("%s %d", players[i].name, &players[i].score);
    }

    // Sort the array using the compare function
    qsort(players, n, sizeof(struct Player), compare);

    // Print the sorted players
    for (int i = 0; i < n; i++) {
        printf("%s %d\n", players[i].name, players[i].score);
    }

    return 0;
}
