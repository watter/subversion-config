subversion-config
=================

Scripts de configuração svn que resolvem alguns problemas comuns:

 * pre-commit + bloqueia_extensao.py + trac-pre-commit-hook

   * Verificação de Codificação de Caracteres - A velha briga Latin1 versus UTF8
   * Validação do Tamanho de Mensagem de Commit - Só caracteres válidos são contados :D
   * Integração com TRAC - Cada commit deve ter um tíquete associado aumentando a rastreabilidade do código
   * Bloqueia extensões Cadastradas - Impede a entrada de arquivos binários (em sua maioria)

 * pos-commit + trac-post-commit-hook

  * Integração com TRAC - permite que o desenvolvedor referencie outro tíquete aberto ou mesmo feche o tíquete a partir da mensagem de commit.
