<template>
    <div class="card">
        <header class="card-header">
            {{ reservation.id }}
        </header>

        <div class="card-content">
            <div class="content">
                {{ reservation.guest_count }} guests
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Reservation } from "@/types/reservation";
import { get } from "@/core/api";

@Component
export default class ReservationEntry extends Vue {
    @Prop() private reservation!: Reservation;

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

