import { request } from "@/utils/service"
import type * as Table from "./types/user-manage"

/** 增 */
export function createTableDataApi(data: Table.ICreateTableRequestData) {
  return request<Table.createTableResponseData>({
    url: "user-manage/add",
    // url: "table",
    method: "post",
    data
  })
}

/** 删 */
export function deleteTableDataApi(id: string) {
  return request<Table.deleteTableResponseData>({
    url: `user-manage/delete/${id}`,
    // url: `table/${id}`,
    method: "delete"
  })
}

/** 改 */
export function updateTableDataApi(data: Table.IUpdateTableRequestData) {
  return request<Table.upDateTableResponseData>({
    url: "user-manage/update",
    // url: "table",
    method: "put",
    data
  })
}

/** 查 */
export function getTableDataApi(params: Table.IGetTableRequestData) {
  return request<Table.GetTableResponseData>({
    url: "user-manage/list",
    // url: "table",
    method: "get",
    params
  })
}
