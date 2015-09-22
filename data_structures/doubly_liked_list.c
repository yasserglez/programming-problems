/* Based on Introduction to Algorithms, 2nd edition, Section 10.2. */

#include <stdio.h>
#include <stdlib.h>


typedef struct linked_list_node {
    int key;
    struct linked_list_node *prev;
    struct linked_list_node *next;
} linked_list_node;


typedef struct {
    linked_list_node *head;
    linked_list_node *tail;
} linked_list;


linked_list_node *linked_list_node_alloc(int key)
{
    linked_list_node *node;

    node = malloc(sizeof(*node));
    if (node != NULL) {
        node->key = key;
        node->next = NULL;
        node->prev = NULL;
    }

    return node;
}


void linked_list_node_free(linked_list_node *node)
{
    free(node);
}


linked_list *linked_list_alloc()
{
    linked_list *list;

    list = malloc(sizeof(*list));
    if (list != NULL) {
        list->head = NULL;
        list->tail = NULL;
    }

    return list;
}


void linked_list_free(linked_list *list)
{
    linked_list_node *curr_node, *tmp;

    curr_node = list->head;
    while (curr_node != NULL) {
        tmp = curr_node;
        curr_node = curr_node->next;
        linked_list_node_free(tmp);
    }
    free(list);
}


linked_list_node *linked_list_search(linked_list *list, int k)
{
    linked_list_node *curr_node;

    curr_node = list->head;
    while (curr_node != NULL && curr_node->key != k) {
        curr_node = curr_node->next;
    }

    return curr_node;
}


void linked_list_insert(linked_list *list, linked_list_node *node)
{
    node->next = list->head;
    if (list->head != NULL) {
        list->head->prev = node;
    }
    list->head = node;
    list->head->prev = NULL;
}


void linked_list_delete(linked_list *list, linked_list_node *node)
{
    if (node->prev != NULL) {
        node->prev->next = node->next;
    }
    if (node->next != NULL) {
        node->next->prev = node->prev;
    }
    if (list->head == node) {
        list->head = node->next;
    }
}


void linked_list_print(linked_list *list)
{
    linked_list_node *curr_node;

    curr_node = list->head;
    while (curr_node != NULL) {
        printf("%d\n", curr_node->key);
        curr_node = curr_node->next;
    }
}


int main(void)
{
    linked_list *list;
    linked_list_node *node;
    int i, values[] = { 1, 4, 16, 9 };

    list = linked_list_alloc();
    for (i = 0; i < 4; i++) {
        node = linked_list_node_alloc(values[i]);
        if (node == NULL) exit(EXIT_FAILURE);
        linked_list_insert(list, node);
    }
    linked_list_print(list);

    node = linked_list_node_alloc(25);
    if (node == NULL) exit(EXIT_FAILURE);
    linked_list_insert(list, node);
    printf("\n");
    linked_list_print(list);

    node = linked_list_search(list, 4);
    linked_list_delete(list, node);
    linked_list_node_free(node);
    printf("\n");
    linked_list_print(list);

    linked_list_free(list);

    return EXIT_SUCCESS;
}
