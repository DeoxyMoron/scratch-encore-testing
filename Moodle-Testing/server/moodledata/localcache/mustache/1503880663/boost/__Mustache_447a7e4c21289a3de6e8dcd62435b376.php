<?php

class __Mustache_447a7e4c21289a3de6e8dcd62435b376 extends Mustache_Template
{
    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $buffer = '';
        $blocksContext = array();

        $buffer .= $indent . '<div class="form-empty">
';
        $buffer .= $indent . '    <input type="hidden" name="';
        $value = $this->resolveValue($context->find('name'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '" id="';
        $value = $this->resolveValue($context->find('id'), $context);
        $buffer .= call_user_func($this->mustache->getEscape(), $value);
        $buffer .= '" value="">
';
        $buffer .= $indent . '</div>
';

        return $buffer;
    }
}
