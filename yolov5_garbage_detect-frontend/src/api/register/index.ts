import { request } from "@/utils/service"
import type * as Register from "./types/register"

/** 获取注册验证码 */
export function getRegisterCodeApi(email: string) {
  return request<Register.RegisterCodeResponseData>({
    url: `auth/register/captcha?email=${email}`,
    method: "get"
  })
}

/** 注册 */
export function registerApi(data: Register.IRegisterRequestData) {
  return request<Register.RegisterResponseData>({
    url: "auth/user/register",
    method: "post",
    data
  })
}
