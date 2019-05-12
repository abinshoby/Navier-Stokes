#include <stdlib.h>
#include<stdio.h>
 
typedef struct {
    unsigned long long int first;
    unsigned long long int second;
} edge;
 
void spanning_tree_recursive(const edge *edges, unsigned long long int size, 
        unsigned long long int order, unsigned long long int *visited, unsigned long long int *tree,
        unsigned long long int vertex, long long int edge, unsigned long long int *len)
{
    unsigned long long int e;
    visited[vertex] = 1;
    if (edge != -1) {
        tree[(*len)++] = edge;
    }
    for (e = 0; e < size; e++) {
        if (edges[e].first == vertex || edges[e].second == vertex) {
            unsigned long long int neighbour = edges[e].first == vertex ?
                edges[e].second : edges[e].first;
            if (!visited[neighbour]) {
                spanning_tree_recursive(edges, size, order, visited, tree, 
                        neighbour, e, len);
            }
        }
    }
}
 
unsigned long long int spanning_tree(const edge *edges, unsigned long long  int size, unsigned  long long int order,
        unsigned long long int **tree)
{
    unsigned long long int *visited = calloc(order, sizeof(unsigned  long long int));
    *tree = malloc((order - 1) * sizeof(unsigned long long int));
    unsigned long long int len = 0;
    if (visited == NULL || *tree == NULL) {
        free(visited);
        free(*tree);
        *tree = NULL;
        return 0;
    }
    spanning_tree_recursive(edges, size, order, visited, *tree, 0, -1, &len);
    free(visited);
    return len;
}
/* Calculate the nth triangular number T(n) */
unsigned long long int triangular_number(unsigned long long int n)
{
    return (n * (n + 1)) / 2;
}
 
/* Construct a complete graph on v vertices */
unsigned long long int complete_graph(unsigned long long int v, edge **edges)
{
    unsigned long long int n = triangular_number(v - 1);
    unsigned long long int i, j, k;
    *edges = malloc(n * sizeof(edge));
    if (edges != NULL) {
        for (i = 0, k = 0; i < v - 1; i++) {
            for (j = i + 1; j < v; j++) {
                (*edges)[k].first = i;
                (*edges)[k].second = j;
                k++;
            }
        }
    }
    else {
        n = 0;
    }
    return n;
}
 
int main(void)
{
    edge *edges;
    const unsigned long long int order = 1000; /* Vertices */
    const unsigned long long int size = complete_graph(1000, &edges); /* Edges */
    unsigned long long int *tree;
    unsigned long long int tree_size = spanning_tree(edges, size, order, &tree);
    unsigned long long int e;
    for (e = 0; e < tree_size; e++) {
        printf("(%llu, %llu) ", edges[tree[e]].first, edges[tree[e]].second);
    }
    printf("\n");
    free(edges);
    free(tree);
    return 0;
}