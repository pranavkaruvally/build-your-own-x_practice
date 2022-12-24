#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "hash_table.h"

static ht_item* ht_new_item(const char* k, const char* v) {
    ht_item *i = malloc(sizeof(ht_item));
    i->key = strdup(k);
    i->value = strdup(v);

    return i;
}

ht_hash_table* ht_new() {
    ht_hash_table *ht = malloc(sizeof(ht_hash_table));

    ht->size = 53;
    ht->count = 0;
    ht->items = calloc((size_t)ht->size, sizeof(ht_item*));
    return ht;
}

static void ht_delete_item(ht_item* i) {
    free(i->key);
    free(i->value);
    free(i);
}

void ht_delete_hash_table(ht_hash_table* ht) {
    for (int i=0; i < ht->size; i++) {
        ht_item *item = ht->items[i];
        if (item != NULL)
            ht_delete_item(item);
    }
    free(ht->items);
    free(ht);
}

static int hash(const char* s, const int a, const int num_buckets) {
    long hash = 0;
    const int len_s = strlen(s);
    for (int i=0; i<len_s; i++)
        hash += (long)pow(a, len_s - (i+1)) * s[i];
    
    hash = hash % num_buckets;
    return hash;
}
