<template>
    <div class="card">
        <header class="card-header">
            {{ customer.name }}
        </header>

        <div class="card-content">
            <div class="content">
                {{ customer.email_address }}
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Customer } from "@/types/customer";
import { get } from "@/core/api";

@Component
export default class CustomerEntry extends Vue {
    @Prop() private customer!: Customer;

}
</script>

<style scoped lang="scss">
$card-header-background-color: #eee;

@import "node_modules/bulma/bulma.sass";

.card-header {
  padding: 0.5rem 0.75rem;
}

.card {
  border: 1px solid #ddd;
  margin: 1rem;
}
</style>
