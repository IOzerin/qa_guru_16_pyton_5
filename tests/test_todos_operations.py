from selene import browser, have, be


def test_complete_todo():
    browser.open('/')
    browser.element('[class="new-todo"]').should(be.blank)

    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('[class="todo-list"]>li').with_(timeout=browser.config.timeout*2).should(have.size(3))

    # Проверяем каждый элемент
    '''
    browser.all('[class="todo-list"]>li').first.should(have.exact_text('a'))
    browser.all('[class="todo-list"]>li').second.should(have.exact_text('b'))
    browser.all('[class="todo-list"]>li')[2].should(have.exact_text('c'))
    '''

    # Либо проверяем сразу все элементы к text добавляется s
    # так как нужно проверить несколько значений
    browser.all('[class="todo-list"]>li').should(have.exact_texts('a', 'b', 'c'))

    '''
    # кликнуть по кружочку у второго элемента, что бы отметить задачу выполненной
    # browser.all('[class="todo-list"]>li').second.element('.toggle').click()
    '''

    # Либо найти элемент по содержащемуся тексту и кликнуть там
    browser.all('[class="todo-list"]>li').element_by(have.exact_text('b')).element('.toggle').click()
    

    browser.all('[class="todo-list"]>li').by(have.css_class('completed')).should(have.exact_texts('b'))
    browser.all('[class="todo-list"]>li').by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))

