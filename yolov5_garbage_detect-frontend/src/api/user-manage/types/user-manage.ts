export interface ICreateTableRequestData {
  username: string
  password: string
  email: string
  roles?: string
}

export interface IUpdateTableRequestData {
  id: string
  username: string
  email?: string
  status?: boolean
  password?: string
  roles?: string
}

export interface IGetTableRequestData {
  /** 当前页码 */
  currentPage: number
  /** 查询条数 */
  size: number
  /** 查询参数：用户名 */
  username?: string
  /** 查询参数：邮箱 */
  email?: string
}

export interface IGetTableData {
  createTime: string
  email: string
  id: string
  // phone: string
  roles: string
  status: boolean
  username: string
}

export type GetTableResponseData = IApiResponseData<{
  list: IGetTableData[]
  total: number
}>

export type createTableResponseData = IApiResponseData<string>
export type deleteTableResponseData = IApiResponseData<string>
export type upDateTableResponseData = IApiResponseData<string>
