import { defineAsyncComponent, type AsyncComponentLoader } from "vue";

import ErrorWidget from "@/components/Widget/ErrorWidget.vue";
import LoadingWidget from "@/components/Widget/LoadingWidget.vue";

export const getWidget = <T = string>(type: T): AsyncComponentLoader => {
    return defineAsyncComponent({
        loader: () => import(`../../widgets/default/${type}.vue`).then((m) => m.default).catch(() => import("@/components/Widget/ErrorWidget.vue")),
        errorComponent: ErrorWidget,
        loadingComponent: LoadingWidget,
    });
};
