from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

from app.models.user import User


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])


class RegisterForm(LoginForm):
    nickname = StringField(validators=[DataRequired(), Length(2, 10,message='昵称至少需要两个，最多需要10个')])

# 业务验证器
    def validate_email(self, field):
        # 查询数据库
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已经被注册')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise  ValidationError('已经这个用户名')

