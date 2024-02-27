<script lang="ts" setup>
import { ref } from "vue"
import { useUserStore } from "@/store/modules/user"
import AdminDashboard from "./admin/index.vue"
import UserDashboard from "./user/index.vue"

type CurrentRoleType = "admin" | "user"

const userStore = useUserStore()
const currentRole = ref<CurrentRoleType>("admin")
if (!userStore.roles.includes("admin")) {
  currentRole.value = "user"
}
</script>

<template>
  <component :is="currentRole === 'admin' ? AdminDashboard : UserDashboard" />
</template>
