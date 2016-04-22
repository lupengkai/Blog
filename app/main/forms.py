from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name', validators=[Required()])
    # 可选参数 validators 指定一个由验证函数组成的列表,在接受用户提交的数据之前验证数据。验证函数 Required() 确保提交的字段不为空。
    submit = SubmitField('Submit')
