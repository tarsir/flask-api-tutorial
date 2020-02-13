<template>
    <div class="card">
        <header class="card-header">
            {{ restaurant.name }}
        </header>

        <div class="card-content">
            <div class="content">
                {{ restaurant.seat_count }} seats
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Restaurant } from "@/types/restaurant";
import { get } from "@/core/api";

@Component
export default class RestaurantEntry extends Vue {
    @Prop() private restaurant!: Restaurant;

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
