export interface IRegisterRequestData {
  username: string
  email: string
  /** 密码 */
  password: string
  confirm_password: string
  /** 验证码 */
  captcha: string
}

export type RegisterCodeResponseData = IApiResponseData<string>

export type RegisterResponseData = IApiResponseData<{ token: string }>
