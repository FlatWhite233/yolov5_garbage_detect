import { request } from "@/utils/service"
import type * as Detect from "./types/detect"

/** 获取当前调用权重 */
export function getCurrentWeightsApi() {
  return request<Detect.GetCurrentWeightsResponseData>({
    url: "detect/weights/current",
    method: "get"
  })
}

/** 获取所有可调用权重 */
export function getAllEnableWeightsApi() {
  return request<Detect.GetEnableWeightsResponseData>({
    url: "detect/weights/list",
    method: "get"
  })
}

/** 切换权重 */
export function switchWeightsApi(data: Detect.ISwitchRoleRequestData) {
  return request<Detect.SwitchWeightsResponseData>({
    url: "detect/weights/switch",
    method: "post",
    data
  })
}
