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
</script>

<style scoped lang="scss">
@import "node_modules/bulma/bulma.sass";
</style>

