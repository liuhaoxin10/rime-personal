-- 手机九键：连续按 GHI 键（数字 4）时，每次对应一个“哈”。
-- 也兼容九键划出的 h；原有候选仍可继续选择。
local function mobile_laugh(input, env)
    local context = env.engine.context
    local code = context.input
    local composition = context.composition

    if not context:get_option("ascii_mode")
        and (code:match("^4+$") or code:match("^[hH]+$"))
        and not composition:empty()
    then
        local segment = composition:back()
        -- 仅处理完整、尚未分段选字的输入，避免覆盖已经选好的前半句。
        if segment.start == 0 and segment._end == #code and context.caret_pos == #code then
            yield(Candidate("mobile_laugh", 0, #code, string.rep("哈", #code), ""))
        end
    end

    for candidate in input:iter() do
        yield(candidate)
    end
end

return mobile_laugh
