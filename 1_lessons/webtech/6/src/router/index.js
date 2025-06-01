import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Auth from "@/components/Auth.vue";
import Account from "@/components/Account.vue";
import { auth } from "../firebase";

const routes = [
    {
        path: "/",
        component: Home
    },
    {
        path: "/account",
        component: Account,
        meta: { requiresAuth: true }
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some((rec) => rec.meta.requiresAuth);
    const currentUser = auth.currentUser;

    if (requiresAuth && !currentUser) {
        next("/auth");
    } else if (to.path === "/auth" && currentUser) {
        next("/");
    } else {
        next();
    }
});

export default router;
