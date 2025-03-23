import {z} from "zod"

export const IdSchema = z.union([z.coerce.number(), z.string().uuid()])
export type Id = z.infer<typeof IdSchema>
