# Generated by Django 3.0.8 on 2020-11-05 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0045_auto_20201019_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeinvoiceitem',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='financeinvoiceitem',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='financeinvoiceitem',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='financeorderitem',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='financeorderitem',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='financeorderitem',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='organizationappointment',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='organizationappointment',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='organizationappointmentprice',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='organizationclasspass',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='organizationclasspass',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='organizationclasspass',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='organizationmembership',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='organizationmembership',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='organizationmembership',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='organizationsubscription',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='organizationsubscription',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='organizationsubscription',
            name='organization_membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.OrganizationMembership'),
        ),
        migrations.AlterField(
            model_name='organizationsubscriptionprice',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='scheduleeventticket',
            name='deletable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scheduleeventticket',
            name='finance_costcenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceCostCenter'),
        ),
        migrations.AlterField(
            model_name='scheduleeventticket',
            name='finance_glaccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceGLAccount'),
        ),
        migrations.AlterField(
            model_name='scheduleeventticket',
            name='finance_tax_rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costasiella.FinanceTaxRate'),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='schedule_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_items', to='costasiella.ScheduleEvent'),
        ),
    ]