export interface ISwitchRoleRequestData {
  /** admin 或 user */
  role: string
}

export type ISwitchRoleResponseData = IApiResponseData<{
  username: string
  token: string
  roles: string[]
}>
